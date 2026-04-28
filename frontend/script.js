document.getElementById("flightForm").addEventListener("submit", async function(e){

e.preventDefault()

const data = {
    source: document.getElementById("source").value,
    destination: document.getElementById("destination").value,
    stops: parseInt(document.getElementById("stops").value),
    date: document.getElementById("date").value,
    departure_time: document.getElementById("time").value
}

try {

const response = await fetch("http://127.0.0.1:8000/predict",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(data)
})

const result = await response.json()

document.getElementById("price").innerText =
"Predicted Price: ₹ " + result.predicted_price

const reasonList = document.getElementById("reasons")
reasonList.innerHTML=""

result.reason.forEach(r=>{
let li=document.createElement("li")
li.innerText=r
reasonList.appendChild(li)
})

} catch(error){

console.error(error)

document.getElementById("price").innerText =
"Error connecting to backend"

}

})