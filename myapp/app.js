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

const app = express();

// Enable CORS for all routes
app.use(cors());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Route to render the HTML page
app.get('/', (req, res) => {
  res.render('index'); // Render the 'index.ejs' file
});


app.get('/mock-interview', (req, res) => {
    res.render('mock-interview'); // Automatically loads views/mock-interview.ejs
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
       // Return the Python output as JSON
       console.log(`stdout: ${stdout}`);
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
       // Return the Python output as JSON
       console.log(`stdout: ${stdout}`);
       res.json({ pythonOutput: stdout.trim() });  // Trim to remove extra whitespace
  });

});


//RUN PYTHON SCRIPT
app.get('/run-evaluation', (req, res) => {
  exec('python3 ./voicetest/chatRequest.py', (error, stdout, stderr) => {  // Use 'python' for Windows
      if (error) {
          console.error(`Error: ${error.message}`);
          return res.status(500).send(`Error: ${error.message}`);
      }
      if (stderr) {
          console.error(`stderr: ${stderr}`);
          return res.status(500).send(`stderr: ${stderr}`);
      }
      // Parse the JSON output from Python
      console.log(`stdout: ${stdout}`);
      res.json({ pythonOutput: stdout.trim() });  // Trim to remove extra whitespace
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
