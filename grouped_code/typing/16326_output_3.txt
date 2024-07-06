
    for (size_t pos = 0; pos < schema.arguments().size(); ++pos) {
      const auto& argument = schema.arguments()[pos];
      if (pos < inputs.size()) {
        // XXX - this fails to handle generic aggregates
        // and should be replaced with a function isSubvalueOf(ivalue, type)
        // That asks if the specific value is a valid instance of type.
        const TypePtr inputType = incompleteInferTypeFrom(inputs[pos]);
        AT_CHECK(
            inputType->isSubtypeOf(argument.type()),
            "Expected value of type ",
            *argument.type(),
            " for argument '",
            argument.name(),
            "' in position ",
            pos,
            ", but instead got value of type ",
            *inputType,
            ". Declaration: ",
            schema);
      } else if (argument.default_value()) {
        inputs.push_back(*argument.default_value());
      } else {
        AT_ERROR(
            schema.name(),
            "() is missing value for argument '",
            argument.name(),
            "'. Declaration: ",
            schema);
      }
    }
