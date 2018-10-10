`timescale 1ns / 1ps

module RegPC #(parameter BITS = 32) (
	input logic [BITS-1:0] pcIn, 
	input logic stall,CLK,RESET,
	output logic [BITS-1:0] pcOut);

	logic [BITS-1:0] pcTemp;
	
	always_ff@(negedge CLK)
	begin 
	if(RESET) pcTemp <=0;
	else 
	begin
		case(stall)
			1'd0: pcTemp <= pcIn;
			1'd1: pcTemp <= pcTemp;
			default: pcTemp <= pcIn;
		endcase
	end
	end
	assign pcOut = pcTemp;
endmodule