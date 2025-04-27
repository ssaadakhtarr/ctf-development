const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const path = require('path');

const app = express();
const PORT = 3000;
const SECRET = 'some-random-key';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.get('/', (req, res) => {
  res.redirect('/login');
});

app.get('/login', (req, res) => {
  res.render('login');
});

app.post('/login', (req, res) => {
  const { username } = req.body;
  if (!username) return res.redirect('/login');

  const token = jwt.sign({ username, points: 0, attempts: 3 }, SECRET, { expiresIn: '1h' });
  res.cookie('token', token, { httpOnly: true });
  res.redirect('/game');
});

function authenticate(req, res, next) {
  const token = req.cookies.token;
  if (!token) return res.redirect('/login');

  try {
    const decoded = jwt.verify(token, SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    return res.redirect('/login');
  }
}

app.get('/game', authenticate, (req, res) => {
    const msg = req.query.msg;
    res.render('game', { user: req.user, msg });
  });
  

app.post('/buy-points', authenticate, (req, res) => {
    let { user } = req;
    const amount = req.body.amount;
  
    if (parseInt(amount) < 0) {
      return res.redirect('/game?msg=' + encodeURIComponent("You entered a negative number."));
    } else if (amount.length > 2) {
      return res.redirect('/game?msg=' + encodeURIComponent("You can only enter a two digit number."));
    } else if (user.attempts <= 0) {
      return res.redirect('/game?msg=' + encodeURIComponent("You don't have any attempts left."));
    } else {
      user.points += parseInt(amount);
      user.attempts -= 1;
  
      const token = jwt.sign(user, SECRET);
      res.cookie('token', token, { httpOnly: true });
      res.redirect('/game');
    }
  });
  
app.get('/get-flag', authenticate, (req, res) => {
  if (req.user.points > 13371337) {
    res.send('Congrats! Here is your flag: flag{typ3_c0nfu$i0n_g4v3_m3_up}');
  } else {
    res.send('Not enough points to get the flag.');
  }
});

app.get('/logout', (req, res) => {
  res.clearCookie('token');
  res.redirect('/login');
});

app.listen(PORT, () => {
  console.log(`CTF Web App running on http://localhost:${PORT}`);
});
