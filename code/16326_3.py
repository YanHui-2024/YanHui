// why incomplete? You cannot completely recover a type from
// an IValue, List[List[int]] and List[List[Tensor]] will both
// become ivalue.isGenericList() and cannot be recovered.
// The only appropriate place to use this is where you know that
// you are only dealing with a subset of objects where you can recover
// the type, like in the tracer.
TypePtr incompleteInferTypeFrom(const IValue& value) {
  if (value.isTensor()) {
    return CompleteTensorType::create(value.toTensor());
  } else if (value.isDouble()) {
    return FloatType::get();
  } else if (value.isInt()) {
    return IntType::get();
  } else if (value.isBool()) {
    return BoolType::get();
  } else if (value.isString()) {
    return StringType::get();
  } else if (value.isIntList()) {
    return ListType::ofInts();
  } else if (value.isTensorList()) {
    return ListType::ofTensors();
  } else if (value.isBoolList()) {
    return ListType::ofBools();
  } else if (value.isDoubleList()) {
    return ListType::ofFloats();
  } else if (value.isTuple()) {
    return TupleType::create(fmap(value.toTuple()->elements(), incompleteInferTypeFrom));
  } else if (value.isDevice()) {
    return DeviceObjType::get();
  }
  AT_ERROR("Type cannot be accurately recovered from this IValue.");
}