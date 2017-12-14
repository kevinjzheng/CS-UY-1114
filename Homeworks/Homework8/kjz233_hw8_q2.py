'''

Kevin J. Zheng
CS 1114
kjz233

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    old_file = open(complete_weather_filename,"r")
    new_file = open(cleaned_weather_filename,"w")
    #print(oldFile.readline())
    for line in old_file:
        #print(line)
        line_split = line.split(',')
        if line_split[8] == 'T':
            line_split[8] = '0'
        newHeader = line_split[0]+","+line_split[1]+","+line_split[2]+","+line_split[3]+","+line_split[8]
        #print(newHeader)
        print(newHeader,file=new_file)
    old_file.close()
    new_file.close()

#clean_data('weather.csv','clean_imperical_weather.csv')


# Part B
def f_to_c(f_temperature):
    c_temperature = round((float(f_temperature) - 32) * (5/9),2)
    return str(c_temperature) # modify this

def in_to_cm(inches):
    centimeters = round(float(inches) * 2.54,2)
    return str(centimeters) # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    # Similar to clean_data() - read in the file and make a new file with metric values.
    imperial_file = open(imperial_weather_filename,"r")
    metric_file = open(metric_weather_filename,"w")
    print("City,Date,High,Low,Precipitation",file=metric_file)
    line_count = 0
    for line in imperial_file:
        line_split = line.split(',')
        #print(line)
        if line_count != 0:
            line_split[2] = f_to_c(line_split[2])
            line_split[3] = f_to_c(line_split[3])
            line_split[4] = in_to_cm(line_split[4])
            newLine = line_split[0]+','+line_split[1]+','+line_split[2]+','+line_split[3]+','+line_split[4]
            print(newLine,file=metric_file)
        line_count += 1
    imperial_file.close()
    metric_file.close()

#convert_data_to_metric('clean_imperical_weather.csv','clean_metric_weather.csv')


# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    #prints average highs and lows in each month for the given city
    monthList = ['January','February','March','April','May','June','July',"August",'September','October','November','December']
    highList = []
    lowList = []
    #file = open(weather_filename,"r")
    for i in range(1,13):
        file = open(weather_filename, "r")
        highSum = 0
        lowSum = 0
        counter = 0
        for line in file:
            line = line[0:-1]
            #print(line)
            line_split = line.split(',')
            #print(line_split[0])
            if line_split[0] == city:
                date = line_split[1].split('/')
                #print(date)
                month = date[0]
                if int(month) == i:
                    highSum += float(line_split[2])
                    lowSum += float(line_split[3])
                    counter += 1
        highList.append(round(highSum/counter,2))
        lowList.append(round(lowSum/counter,2))

    if unit_type == 'metric':
        unit = "C°"
    else:
        unit = "F°"

    print("Average temperatures for",city,":")
    for i in range(12):
        print(monthList[i],":",str(highList[i])+str(unit), "High,", str(lowList[i])+str(unit),"Low")

    file.close()
#print_averages_per_month("San Francisco","clean_imperical_weather.csv","imperial")

# Part D
# Write your question (as a comment), and implement a function to answer it
# Given two cities, which has a higher average rainfall?
def print_higher_rainfall(city1,city2,weather_filename):
    file = open(weather_filename,'r')
    precipSum1 = 0
    precipSum2 = 0
    counter1 = 0
    counter2 = 0
    avgPrecip = []
    for line in file:
        line = line.strip("\n")
        # print(line)
        line_split = line.split(',')
        # print(line_split[0])
        if line_split[0] == city1:
            precipSum1 += float(line_split[4])
            counter1 += 1
        if line_split[0] == city2:
            precipSum2 += float(line_split[4])
            counter2 += 1
    avgPrecip.append(round(precipSum1/counter1,2))
    avgPrecip.append(round(precipSum2/counter2,2))
    #print(precipSum1)
    #print(precipSum2)
    #print(avgPrecip)
    if avgPrecip[0] > avgPrecip [1]:
        city = city1
        avgRainfall = avgPrecip[0]
    else:
        city = city2
        avgRainfall = avgPrecip[1]

    print(city,"has a higher average rainfall of",avgRainfall)

    file.close()

def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print()
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print()
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print()
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")
    print()

    print ("Running Part D")
    print()
    # add your code here
    print_higher_rainfall("San Francisco", "New York","weather in imperial.csv")
    print()
    print_higher_rainfall("San Francisco","San Jose","weather in imperial.csv")
    print()
    print_higher_rainfall("San Jose","New York","weather in imperial.csv")
    print()

main()
