{ pkgs ? import <nixpkgs> {} }:
let
  python-with-my-packages = pkgs.python3.withPackages (p: with p; [
    boto3
    markdown
    # other python packages you want
  ]);
  elixir = pkgs.beam.packages.erlangR24.elixir_1_13;
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
    pkgs.awscli
    elixir
    # other dependencies
  ];
  shellHook = ''
    PYTHONPATH=${python-with-my-packages}/${python-with-my-packages.sitePackages}
  '';
}
