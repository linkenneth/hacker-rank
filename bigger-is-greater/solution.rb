#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w)
  w.reverse.chars.each.with_index do |c_i, i|
    j = i - 1
    while j >= 0
      # swap if good
      if w[j] > c_i
        w[i], w[j] = w[j], w[i]
        return w
      end
      j -= 1
    end
  end
  return 'no answer'
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

T = gets.strip.to_i

T.times do |t_itr|
  w = gets.chomp

  result = biggerIsGreater w

  fptr.write result
  fptr.write "\n"
end

fptr.close()
