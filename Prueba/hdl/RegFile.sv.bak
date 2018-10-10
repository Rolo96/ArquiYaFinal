`timescale 1ns / 1ps

module RegFile(
	input logic clk, //clock
	input logic we3, //habilitar escritura
	input logic [3:0] a1, a2, wa3, //a1:registro 1; a2:registro2; wa3:registro destino
	input logic [31:0] wd3, r15, //valor a guardar; r15 = pc+8
	output logic [31:0] rd1, rd2 //valores de salidas leidas
	);
	
	logic [31:0] rf[14:0]; //16 registros de 32 bits

	always_ff @(posedge clk)
		if (we3) rf[wa3] <= wd3;
	
	assign rd1 = (a1 == 4'b1111) ? r15 : rf[a1];
	assign rd2 = (a2 == 4'b1111) ? r15 : rf[a2];
endmodule
