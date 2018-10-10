`timescale 1ns / 1ps

module DisplayController
(input logic inControl,
input logic [31:0] inMicro,
input logic [18:0] inVGA,
output logic [18:0] out);

logic [18:0] temp;


always_comb
begin
	if (inControl != 1'b0 & inControl != 1'b1 )
		temp <= inVGA;
	else
		temp <= inMicro[18:0];
end

assign out = temp;

endmodule