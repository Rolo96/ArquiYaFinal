`timescale 1ns / 1ps

module RegFile(
	input logic clk,reset, //clock
	input logic we3, //habilitar escritura
	input logic [3:0] a1, a2, wa3, //a1:registro 1; a2:registro2; wa3:registro destino
	input logic [31:0] wd3, r15, //valor a guardar; r15 = pc+8
	output logic [31:0] rd1, rd2 //valores de salidas leidas
	);
	
	logic [31:0] rf[14:0]; //16 registros de 32 bits

	
	always_ff @(posedge clk)begin
		if(reset)begin
				rf[0] <= 32'b0;
				rf[1] <= 32'b0;
				rf[2] <= 32'b0;
				rf[3] <= 32'b0;
				rf[4] <= 32'd5;
				rf[5] <= 32'b0;
				rf[6] <= 32'b0;
				rf[7] <= 32'b0;
				rf[8] <= 32'b0;
				rf[9] <= 32'b0;
				rf[10] <= 32'b0;
				rf[11] <= 32'b0;
				rf[12] <= 32'b0;
				rf[13] <= 32'd4;
				rf[14] <= 32'd8;
		end
		else if (we3) rf[wa3] <= wd3;
end
	assign rd1 = (a1 == 4'b1111) ? r15 : rf[a1];
	assign rd2 = (a2 == 4'b1111) ? r15 : rf[a2];
endmodule
