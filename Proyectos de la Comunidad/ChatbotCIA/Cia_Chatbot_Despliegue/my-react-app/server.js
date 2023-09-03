import express from 'express';
import { spawn } from 'child_process';
import cors from 'cors';

const app = express();
const PORT = 8001;

app.use(express.json());
app.use(cors());

app.post('/embeddings', (req, res) => {
  const { text } = req.body;

  // Llamar al archivo de Python "embedding.py"
  const pythonProcess = spawn('python', ['embedding.py']);

  let output = '';

  pythonProcess.stdout.on('data', (data) => {
    output += data.toString();
  });

  pythonProcess.stdout.on('end', () => {
    // Enviar la respuesta al cliente con la cabecera de codificación de caracteres adecuada
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.send(JSON.stringify({ result: output }));
  });

  // Enviar el texto de entrada al script de Python
  pythonProcess.stdin.write(text);
  pythonProcess.stdin.end();
});

/*
app.post('/embeddingsvoiceservice', (req, res) => {
  const { text } = req.body;

  // Llamar al archivo de Python "embedding.py"
  const pythonProcess = spawn('python', ['embeddingsvoiceservice.py']);

  let output = '';

  pythonProcess.stdout.on('data', (data) => {
    output += data.toString();
  });

  pythonProcess.stdout.on('end', () => {
    // Enviar la respuesta al cliente con la cabecera de codificación de caracteres adecuada
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.send(JSON.stringify({ result: output }));
  });

  // Enviar el texto de entrada al script de Python
  pythonProcess.stdin.write(text);
  pythonProcess.stdin.end();
});

*/

app.listen(PORT, () => console.log(`Server running on port: ${PORT}`));
