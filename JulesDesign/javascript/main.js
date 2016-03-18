(function() {
	var app = angular.module("whattodo", []);

	app.controller("doingwhat", function() {
		this.test  = 1;
		this.VCenter  = function() {
			var height = $(window).height();
			$("#input").css("top", height/2 - 155);
		};
		$(window).resize(this.VCenter);
		$(window).load(this.VCenter);
	});
})();

