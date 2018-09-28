`timescale 1ns / 1ps

module Mux3 #(parameter BITS = 32) (
	input logic [BITS-1:0] d0, d1, d2,
	input logic [1:0] s, 
	output logic [BITS-1:0] y);

	logic [BITS-1:0] yTemp;
	
	always_comb
	begin 
		case(s)
			2'd0: yTemp <= d0;
			2'd1: yTemp <= d1;
			2'd2: yTemp <= d2;
			default: yTemp <= d0;
		endcase
	end
	assign y = yTemp;
endmodule