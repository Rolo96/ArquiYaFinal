module frecuencyDivider(
	input wire i_clk,
   output wire o_clk
);	
	reg clk_temp = 0;
	
	always_ff@(posedge i_clk)
	begin
		clk_temp <= ~o_clk;
	end
	
	assign o_clk = clk_temp;
endmodule