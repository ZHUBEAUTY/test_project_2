const express = require("express");
const auth = require("./middleware/auth");
const routes = require("./routes/taskRoutes");

const app = express();

app.use(routes);
app.use(auth);

app.listen(3000);
