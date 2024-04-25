(module
  (func $add (export "add") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.add
  )
  (func $sub (export "sub") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.sub
  )
  (func $mul (export "mul") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.mul
  )
  (func $div (export "div") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.div_s
  )
  (func $mod (export "mod") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.rem_s
  )
)
