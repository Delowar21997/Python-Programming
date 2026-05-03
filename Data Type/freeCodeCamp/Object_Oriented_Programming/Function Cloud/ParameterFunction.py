def simple_interest(principal, rate, time):
    print(f"Calculating simple interest for principal={principal}, rate={rate}%, time={time} years")
    interest = (principal * rate * time) / 100
    print(f"Simple interest calculated: {interest}")
simple_interest(1000, 5, 3)
print('-*-' *25)
simple_interest(1500, 4.5, 2)