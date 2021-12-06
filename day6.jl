f = open("input6.txt")
inp = read(f, String)
close(f)

inp = [parse(Int32, i) for i in split(inp,',')]
track = Dict((i, 0) for i in 0:8)

for i in inp
    track[i] += 1
end

for i in 1:256
    track[(i+6)%9] += track[(i-1)%9]
    
end

println(sum(values(track)))