#!/usr/bin/node

module.exports = class Rectangle {
	contructor (w, h) {
		if (this.w > 0 && this.h > 0) {
			this.width = w;
			this.height = h;
		}
	}
};
