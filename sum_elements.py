class SumElements:
    MAX = 100

    def __init__(self):
        self.arr = []

    def calculate_sum(self):
        result = 0
        for num in self.arr:
            result += num
        return result

    def get_input(self):
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if not 1 <= n <= self.MAX:
                print("Invalid input. Please provide a digit ranging from 1 to 100.")
                return False

            print(f"Enter {n} integers:")
            for _ in range(n):
                try:
                    self.arr.append(int(input()))
                except ValueError:
                    print("Invalid input. Please enter valid integers.")
                    return False

            return True

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return False

    def main(self):
        if self.get_input():
            total = self.calculate_sum()
            print("Sum of the numbers:", total)

if __name__ == "__main__":
    SumElements().main()