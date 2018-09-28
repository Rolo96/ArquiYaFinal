`timescale 1ns / 1ps

module Mux2 #(parameter BITS = 32) (
	input logic [BITS-1:0] d0, d1, 
	input logic s, 
	output logic [BITS-1:0] y);

	assign y = s ? d1 : d0; 
endmodule
