package HandleForm;
# forms-lib.pl
# Decodes URLs and unpacks from input.
# Read the form contents into $input, decodes it, unpacks it,
# and returns it as an associative array.

sub GetFormInput
{
  my(%input);
  $input = &ReadInput();
  %input = &ParseInput($input) if $input;
  return(%input);
}

sub ReadInput
{
  my($method, $input, $length);
  $method = $ENV{'REQUEST_METHOD'};
  if($method eq 'GET')
  {
    $input = $ENV{'QUERY_STRING'};
  }
  elsif ($method eq 'POST')
  {
    $length = $ENV{'CONTENT_LENGTH'};
    read(STDIN, $input, $length);
  }

  return($input);
}

sub ParseInput
{
  my($input) = @_;
  my(@pairs);
  my(%input);
  @pairs = split('&',$input);
  foreach $pair (@pairs)
  {
    # convert all plus signs to spaces.
    $pair =~ s/\+/ /g;

    # split into a key and a value.
    ($key, $value) = split('=', $pair, 2);

    # Convert hex numbers to alphanumeric.
    $key =~ s/%(..)/pack("c", hex($1))/ge;
    #$value =~ s/%(..)/pack("c", hex($1))/ge;
    $value =~ s/%([\da-fA-F][\da-fA-F])/pack("c", hex($1))/ge;

    # handle multiple values, separated by newlines.
    $input{$key} .= "\n" if defined($input{$key});

    # associate keys and values
    $input{$key} = $value;
  }
  return (%input);
}

1;