#!/bin/ruby

require 'json'
require 'stringio'

# Complete the getMinimumCost function below.
def getMinimumCost(k, c)
  c.sort.reverse.map.with_index do |cost, i|
    cost * (1 + i / k)
  end.sum
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

nk = gets.rstrip.split

n = nk[0].to_i

k = nk[1].to_i

c = gets.rstrip.split(' ').map(&:to_i)

minimumCost = getMinimumCost k, c

fptr.write minimumCost
fptr.write "\n"

fptr.close()
