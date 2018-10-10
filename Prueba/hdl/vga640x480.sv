	module vga640x480(
	input logic i_clk,
   input logic i_rst,           
   output logic o_hs,           // horizontal sync
   output logic o_vs,           // vertical sync
   output logic o_blanking,     
   output logic o_sync,
	output logic o_clk,
	output logic [7:0] o_r,
	output logic [7:0] o_g,
	output logic [7:0] o_b,
	output logic [17:0] A_VGA,
	input logic [31:0] RD_VGA
);	 
		
	//	Horizontal Parameter	( Pixel )
	parameter	H_SYNC_FRONT =	640 + 96 + 48 + 16;
	parameter	H_SYNC_CYC	 =	96;
	parameter	H_SYNC_BACK	 =	96 + 48;
	parameter	H_SYNC_ACT	 =	320 + 96 + 48;	
	parameter	H_SYNC_ACT2	 =	640 + 96 + 48;	
	parameter	H_SYNC_TOTAL =	800;

	//	Virtical Parameter		( Line )
	parameter	V_SYNC_FRONT =	2+ 33 + 480 + 10;
	parameter	V_SYNC_CYC	 =	2;
	parameter	V_SYNC_BACK	 =	2 + 33;
	parameter	V_SYNC_ACT	 =	2+ 33 + 240;
	parameter	V_SYNC_TOTAL =	525; 
	 
	 
   reg [9:0] h_count = 10'b0;  // line position
   reg [9:0] v_count = 10'b0;  // screen position
	logic m_hs,m_vs,zero,one = 1'b0;
	logic [7:0] r = 8'b0;
	logic [7:0] g = 8'b0;
	logic [7:0] b = 8'b0;
	reg [17:0] counter = 18'b0;
	reg [17:0] counter2 = 18'b0;
	reg [17:0] counter3 = 18'd76800;
	
	always_ff@(posedge i_clk)
	begin
		if (!i_rst)
			begin
				h_count <= 10'b0;
				v_count <= 10'b0;
				m_hs <= 1'b0;
				m_vs <= 1'b0;
            zero <= 1'b0;
				one <= 1'b1;
				r <= 8'd0;
				g <= 8'd0;
				b <= 8'd0;
			end
		else
			begin
				zero <= 1'b0;
				one <= 1'b1;
			
				if (h_count == H_SYNC_TOTAL)  // end of line
				begin
					h_count <= 0;
					v_count <= v_count + 1'b1;
            end
            else 
				begin
               h_count <= h_count + 1'b1;
				end
            if (v_count == V_SYNC_TOTAL)  // end of screen
				begin
					v_count <= 0;
					counter = 18'b0;
					counter2 = 18'b0;
					counter3 = 18'd76800;
				end
				
				if (h_count <= H_SYNC_CYC)
				begin
					m_hs <= 0;
				end
				else
				begin
					m_hs <= 1;
				end
				
				if (v_count <= V_SYNC_CYC)
				begin
					m_vs <= 0;
				end
				else
				begin
					m_vs <= 1;
				end
				
				if ((h_count >= H_SYNC_BACK & h_count< H_SYNC_ACT) & (v_count>=V_SYNC_BACK & v_count< V_SYNC_ACT) )
				begin
					counter2 = counter2 + 1'b1;
					counter = counter2;
					b <= RD_VGA[7:0];
					g <= RD_VGA[15:8];
					r <= RD_VGA[23:16];
					//r <= 8'd255;
					//g <= 8'd255;
					//b <= 8'd255;
				end
				else if ((h_count >= H_SYNC_ACT & h_count< H_SYNC_ACT2) & (v_count>=V_SYNC_BACK & v_count< V_SYNC_ACT) )
				begin
					counter3 = counter3 + 1'b1;
					counter = counter3;
					b <= RD_VGA[7:0];
					g <= RD_VGA[15:8];
					r <= RD_VGA[23:16];
					//r <= 8'd255;
					//g <= 8'd255;
					//b <= 8'd255;
				end
				else 
				begin 
					counter2 = counter2;
					counter3 = counter3;
					counter = counter;
					r <= 8'd0;
					g <= 8'd0;
					b <= 8'd0;
				end
				
			end               
	end
	
	assign o_hs = m_hs;
	assign o_vs = m_vs;
	assign o_blanking = one;
	assign o_sync = zero;
	assign o_clk = i_clk;
	assign o_r = r;
	assign o_g = g;
	assign o_b = b;
	assign A_VGA = counter;

endmodule