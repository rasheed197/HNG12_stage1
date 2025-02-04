import httpx


class NumberService: 
    async def get_is_prime(self, number):
        if number == 0 or number == 1:
            return False
        for i in range(2, number):
            if (number % i) == 0:
                # If a factor is found, then number is not a prime number
                return False
        return True

    async def get_is_perfect(self, number):
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        return number == sum

    async def get_is_armstrong(self, number):
        order = len(str(number))
        sum = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        return sum == number

    async def get_digit_sum(self, number):
        return sum(list(map(int, str(number))))

    async def get_is_odd(self, number):
        if number % 2 == 0:
            return False
        return True

    async def get_properties(self, number):
        property = []
        if await self.get_is_armstrong(number):
            property.append("armstrong")
        if await self.get_is_odd(number): 
            property.append("odd")
            return property
        property.append("even")
        return property

    async def get_fun_fact(self, number):
        api_url = f"http://numbersapi.com/{number}/math?json"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            response = response.json()
            return response["text"]