`timescale 1ns / 1ps
module Extend (
	input logic [23:0] InstrD, 
	input logic [1:0] ImmSrcD, 
	output logic [31:0] ExtImm);

	always_comb 
		case(ImmSrcD) 
			// 8-bit inmediato sin signo (POSIBLE ELIMINACION)
			2'b00: ExtImm = {24'b0, InstrD[7:0]}; 
			// 12-bit inmediato sin sugno (POSIBLE ELIMINACION)
			2'b01: ExtImm = {20'b0, InstrD[11:0]}; 
			// 24-bit complemento a dos branch 
			2'b10: ExtImm = {{6{InstrD[23]}}, InstrD[23:0], 2'b00}; 
			//
			2'b11: ExtImm = {10'b0,InstrD[21:0]};
			default: ExtImm = 32'bx; 
		endcase
endmodule