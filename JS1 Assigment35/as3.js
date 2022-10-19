const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    // ages.sort()

// console.log(ages);
// console.log("minuim value is" + Math.min(...ages));
// // console.log("maximum value is" + Math.max(...ages));
// res = ages.slice(4, 5)
// console.log(res);
sum = 0

for (let i of ages) {
    sum = sum + i
}
avrage = sum / ages.length;
console.log(avrage);