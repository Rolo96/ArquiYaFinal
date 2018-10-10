`timescale 1ns / 1ps
module ControlLED (
	input logic d1,  
	output logic y);

	always_comb 
		if(d1==1'b1|d1==1'b0) y = 1'b0;
		else y=1'b1;
endmodule