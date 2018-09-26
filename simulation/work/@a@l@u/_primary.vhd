library verilog;
use verilog.vl_types.all;
entity ALU is
    generic(
        BITS            : integer := 32
    );
    port(
        SrcAE           : in     vl_logic_vector;
        SrcBE           : in     vl_logic_vector;
        ALUControlE     : in     vl_logic_vector(2 downto 0);
        ALUFlags        : out    vl_logic_vector(3 downto 0);
        ALUResultE      : out    vl_logic_vector
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end ALU;
