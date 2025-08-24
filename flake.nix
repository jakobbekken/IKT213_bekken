{
  description = "IKT213 assignments";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        python = pkgs.python313;

      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            (python.withPackages (ps: with ps; [
              opencv4
              numpy
              matplotlib
              tqdm
              jedi-language-server
            ]))
            pkgs.pyright
            pkgs.ruff
          ];
        };
      }
    );
}
