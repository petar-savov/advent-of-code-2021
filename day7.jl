using Statistics, Printf

inp = readline("input7.txt")
inp = [parse(Int32, i) for i in split(inp,',')]

# part 1
println(sum(abs.(inp.-Int(median(inp)))))

# part 2
cost = n -> n*(n+1)/2
c1 = sum(cost.(abs.(inp.-Int(ceil(mean(inp))))))
c2 = sum(cost.(abs.(inp.-Int(floor(mean(inp))))))
@printf("%d", min(c1,c2))
