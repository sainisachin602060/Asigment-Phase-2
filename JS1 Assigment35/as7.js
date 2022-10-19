let result = '';
let values = "ABCDEF0123456789"
for (let i = 0; i <= 5; i++) {
    result += values.charAt(Math.floor(Math.random() * values.length))

}
console.log(result);