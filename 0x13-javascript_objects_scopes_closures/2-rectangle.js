#!/usr/bin/node

module.exports = class Rectangle {
	contructor (w, h) {
		if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
			this.width = 0;
			this.height = 0;
		}
		else {
			this.width = w;
			this.height = h;
		}
	}
};
