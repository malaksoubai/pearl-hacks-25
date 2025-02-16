// const express = require('express')
// const app = express()
// const port = 3000

// app.get('/', (req, res) => {
//   res.send('Hello World!')
// })

// app.listen(port, () => {
//   console.log(`Example app listening on port ${port}`)
// })


const express = require('express');
const cors = require('cors'); // Add this import
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();

app.use(cors());

app.use(express.static(path.join(__dirname, 'public')));

app.use(express.urlencoded({ extended: true })); //parse URL-encoded form data from submission POST 
app.use(express.json()); //clients sends requests with JSON data

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Route to render the HTML page
app.get('/', (req, res) => {
  res.render('index');
});


app.get('/mock-interview', (req, res) => {
    res.render('mock-interview'); // Automatically loads views/mock-interview.ejs
});

app.get('/mentorship', (req, res) => {
  res.render('mentorship');
});

const pythonScriptPath = path.join(__dirname, 'path_to_your_script', 'mentor-match-real.py');

app.post('/find-matches', (req, res) => {
  const { industry_of_interest, skills_of_interest } = req.body;

  const userData = JSON.stringify({
    industry_of_interest,
    skills_of_interest
  });

  exec(`python ${pythonScriptPath} "${userData}"`, (err, stdout, stderr) => {
    if (err) {
      console.error(`Error running Python script: ${stderr}`);
      res.status(500).send('Error running Python script');
      return;
    }

    const result = stdout;
    console.log(result);
    res.render('match-results', { matches: result });
  });
});



//RUN PYTHON SCRIPT - SHOW QUESTION!!
app.get('/run-question', (req, res) => {
  exec('python3 ./voicetest/showQuestion.py', (error, stdout, stderr) => {  // Use 'python' for Windows
      if (error) {
          console.error(`Error: ${error.message}`);
          return res.status(500).send(`Error: ${error.message}`);
      }
      if (stderr) {
          console.error(`stderr: ${stderr}`);
          return res.status(500).send(`stderr: ${stderr}`);
      }
       console.log(`stdout: ${stdout}`); //return output as json
       res.json({ pythonOutput: stdout.trim() });  // Trim to remove extra whitespace
  });
});


//RUN PYTHON SCRIPT - RECORDING!!
app.get('/run-recording', (req, res) => {
  exec('python3 ./voicetest/recording.py', (error, stdout, stderr) => {  // Use 'python' for Windows
      if (error) {
          console.error(`Error: ${error.message}`);
          return res.status(500).send(`Error: ${error.message}`);
      }
      if (stderr) {
          console.error(`stderr: ${stderr}`);
          return res.status(500).send(`stderr: ${stderr}`);
      }
       console.log(`stdout: ${stdout}`);
       res.json({ pythonOutput: stdout.trim() });
  });

});


//RUN PYTHON SCRIPT
app.get('/run-evaluation', (req, res) => {
  exec('python3 ./voicetest/chatRequest.py', (error, stdout, stderr) => { 
      if (error) {
          console.error(`Error: ${error.message}`);
          return res.status(500).send(`Error: ${error.message}`);
      }
      if (stderr) {
          console.error(`stderr: ${stderr}`);
          return res.status(500).send(`stderr: ${stderr}`);
      }
      console.log(`stdout: ${stdout}`);
      res.json({ pythonOutput: stdout.trim() });
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
