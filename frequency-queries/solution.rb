#!/bin/ruby

require 'json'
require 'stringio'
require 'set'

# Complete the freqQuery function below.
def freqQuery(queries)
  data_to_freq = Hash.new(0)
  freq_to_data = Hash.new { |h, a| h[a] = Set.new }

  answers = []
  queries.each do |(op, operand)|
    case op
    when 1
      freq = data_to_freq[operand]
      freq_to_data[freq].delete(operand)
      freq_to_data[freq + 1].add(operand)
      data_to_freq[operand] += 1
    when 2
      freq = data_to_freq[operand]
      if freq > 0
        freq_to_data[freq].delete(operand)
        freq_to_data[freq - 1].add(operand)
        data_to_freq[operand] -= 1
      end
    when 3
      if freq_to_data[operand].empty?
        answers << '0'
      else
        answers << '1'
      end
    end
  end
  answers
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.strip.to_i

queries = Array.new(q)

q.times do |i|
  queries[i] = gets.rstrip.split.map(&:to_i)
end

ans = freqQuery queries

fptr.write ans.join "\n"
fptr.write "\n"

fptr.close()
