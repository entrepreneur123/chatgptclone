//Example of post method implementation
async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

sendButton.addEventListener("click", async () => {
  alert("Hey you clicked!! ");
  questionInput = document.getElementById("questionInput").value;
  document.getElementById("questionInput").value = "";
  document.querySelector(".right2").style.display = "block";
  document.querySelector(".right1").style.display = "none";

  question1.innerHTML = questionInput;
  question2.innerHTML = questionInput;
});

sendButton1.addEventListener("click", () => {
  alert(" you did it !!");
});

//Get ans and populate it over here
let result = postData("/api", { question: "questionInput" });
solution.innerHTML = result.answer;
