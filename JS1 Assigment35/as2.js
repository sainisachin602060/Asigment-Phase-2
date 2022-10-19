const webTechs = ["laptop", "dell", "sess"]
res = webTechs.includes("sass")
if (res == true) {
    console.log("sass is web xss");
} else {
    webTechs.push("sass")
    console.log(webTechs);
    console.log("updated");
}