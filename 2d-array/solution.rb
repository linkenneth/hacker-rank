#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr)
  max_hourglass_sum = -10e9
  arr.each.with_index do |row, r|
    row.each.with_index do |val, c|
      next if r + 2 >= arr.length || c + 2 >= row.length
      hourglass_sum = (
        arr[r][c] +
        arr[r][c + 1] +
        arr[r][c + 2] +
        arr[r + 1][c + 1] +
        arr[r + 2][c] +
        arr[r + 2][c + 1] +
        arr[r + 2][c + 2]
      )
      max_hourglass_sum = [hourglass_sum, max_hourglass_sum].max
    end
  end

  max_hourglass_sum.to_i
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

arr = Array.new(6)

6.times do |i|
    arr[i] = gets.rstrip.split.map(&:to_i)
end

result = hourglassSum arr

fptr.write result
fptr.write "\n"

fptr.close()
