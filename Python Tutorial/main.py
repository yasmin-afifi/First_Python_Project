start_year = int(input('Enter start year = '))
end_year = int(input('Enter end year = '))

age = 0
if end_year >= start_year:
  age = end_year - start_year

print(age)
