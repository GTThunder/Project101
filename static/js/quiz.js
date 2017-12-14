
var currentCategory= ['Vehicles'];
var Questions= [
	// store answer with questions for easier retrieval
    { category: 'Vehicles', question: 'Electric vehicles are more efficient and less polluting', answer: true },
	{ category: 'Vehicles', question: 'Diesel contains sulfur', answer: true },
	{ category: 'Vehicles', question: 'It is preferable to travel to any places regardless of distance by car ', answer: false },
    { category: 'Vehicles', question: 'It is good to warm up by starting the engine several minutes before you drive', answer: false },
	{ category: 'Vehicles', question: 'When it comes to car fuels, biodiesel is better compared to diesel.', answer: true },

];

// when declared over here other functions will see it; it's not best practice to register them in global/window scope, but better than nothing ;)
var count = 0;
var points = 0;
var category;
var question;

//show answer buttons only after clicking start button
function showButtons(){
	document.getElementById('answerT').style.display="";
	document.getElementById('answerF').style.display="";
}

// choose a category and a question
function catAndQuest() {
	start.style.display = 'none';
	showButtons();

	document.getElementById('points').innerHTML= 'Points: ' + (points);
	document.getElementById('count').innerHTML= 'Question ' + (++count) + ' \/ 5';

	currentCategory = Questions.map(function(question) {
    	return question.category;
    });
	category = currentCategory[Math.floor(Math.random() * currentCategory.length)];
	document.getElementById('category').innerHTML= 'Category: ' + (category);

	var questionList= Questions.filter( function (question){
		return question.category === category;
	});

	question = questionList[Math.floor(Math.random() * questionList.length)];
	document.getElementById('quest').innerHTML= question.question;
}

// create a copy of Questions array
var copy = [].concat(Questions);

// delete used question out of the copy array
function deleteUsed (){
	if(Questions.length > 0) {
		Questions.splice(Questions.indexOf(question),1);
	} else {
		document.getElementById('answerT').style.display="none";
		document.getElementById('answerF').style.display="none";
		document.getElementById('questions').style.display="none";
		document.getElementById('looser').style.display="";
		document.getElementById('reset').style.display="";
	}
}

//user answered question
function answer(value){
	deleteUsed();
	if(value === question.answer) {
		points++;
		if(points==15){
			document.getElementById('answerT').style.display="none";
			document.getElementById('answerF').style.display="none";
			document.getElementById('questions').style.display="none";
			document.getElementById('winner').style.display="";
			document.getElementById('reset').style.display="";
		}
	}
	catAndQuest();
}

//restart the game
function restart(){
	document.location.href="";
}


