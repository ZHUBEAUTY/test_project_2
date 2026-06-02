const express = require("express");
const router = express.Router();

router.get("/tasks", (req, res) => {
    res.send([
        {
            id: 1,
            title: "demo"
        }
    ]);
});

module.exports = router;
