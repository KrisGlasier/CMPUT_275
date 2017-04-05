#!/usr/bin/env bash
rm -f MST.tar.gz
echo "Packing up files:"
tar --exclude __pycache__ -cvzf MST.tar.gz *
echo "Files ready. Upload MST.tar.gz through eclass"
