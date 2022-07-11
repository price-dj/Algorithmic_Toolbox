# Uses python3
import sys

#capacity = 50
#weights = [20, 50, 30]
#values = [60, 100, 120]

def get_optimal_value(capacity, weights, values):
    
    
    value = 0.0
    densityList = [float(x)/float(y) for x, y in zip(values, weights)]
    
    #make a list of lists with weights, values and densities
    totalList = []
    for i in range(len(weights)):
    	totalList.append([weights[i], values[i], densityList[i]])
    
    #sort totalList
    totalList.sort(key=lambda x: x[2], reverse=True)
    
    for i in range(len(totalList)):
    	if capacity == 0:
    		return value
    	amount = min(totalList[i][0], capacity)
    	value += float(amount)*float(totalList[i][2])
    	capacity -= amount
    	totalList[i][0] -= amount
    	
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
