$memo = Hash.new

def string_reduce s
  s.each_index do |i|
    if a[0] != a[1]
      other_char = ('a'..'c').select { |x| x != a[0] and x != a[1] }
      other_char + s
    end
  end
end
