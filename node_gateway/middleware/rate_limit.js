const limits = {};

module.exports = function(req, res, next) {
    const ip = req.headers["x-forwarded-for"] || req.ip;

    if (!limits[ip]) {
        limits[ip] = 0;
    }

    limits[ip] += 1;

    if (limits[ip] > 100) {
        return res.status(429).send("too many requests");
    }

    next();
}
