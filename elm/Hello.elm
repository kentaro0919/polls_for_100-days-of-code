module Hello exposing (..)

import Html exposing (text)

main : Html.Html msg
main =
    3
      |> addOne
      |> add 38
      |> toString
      |> text


addOne : Int -> Int
addOne x =
    x + 1


add : Int -> Int -> Int
add x y =
    x + y