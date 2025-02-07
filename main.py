from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from service import NumberService
import asyncio


app = FastAPI()

number_service = NumberService()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:80",
    "http://localhost:8000",
    "https://number-classification-39yf.onrender.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
                "number": "alphabet",
                "error": True
            },
    )
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    query_parameter = request.query_params._dict["number"]
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        # content=jsonable_encoder({"detail": exc.errors(),  # optionally include the errors
        #         "body": exc.body,
        #          "custom msg": {"Your error message"}}),
        content={
                "number": query_parameter,
                "error": True
            },
    )

@app.get('/api/classify-number')
async def number_class(number: int):
    try:
        fun_fact = await number_service.get_fun_fact(number)
        is_prime = await number_service.get_is_prime(number)
        is_perfect = await number_service.get_is_perfect(number)
        properties = await number_service.get_properties(number)
        digit_sum = await number_service.get_digit_sum(number)
        return JSONResponse(
            content= {
                "number": number,
                "is_prime": is_prime,
                "is_perfect": is_perfect,
                "properties": properties,
                "digit_sum": digit_sum,
                "fun_fact": fun_fact
            },
            status_code=status.HTTP_200_OK
    )
    except Exception:
        return JSONResponse(
            content={
                "msg": "something went wrong",
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    